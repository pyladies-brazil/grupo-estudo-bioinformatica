{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Exercício_A_Vanessa.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM0HL4X4eYKYvlBIXNmam5t"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qhTfyIrnakAW"
      },
      "source": [
        "#**Encontro 04/04/21**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KGW8us64gDDi"
      },
      "source": [
        "###Counting DNA nucleotides"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bTl_CNz7gHDQ"
      },
      "source": [
        "from collections import Counter"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 154
        },
        "id": "2ToPGAfmgn6G",
        "outputId": "e26f672d-ecb6-4d2e-d6a2-3dfa724b4b16"
      },
      "source": [
        "# leitura do arquivo\n",
        "arquivo = open(\"/content/rosalind_dna.txt\", \"r\")\n",
        "dna = arquivo.read()\n",
        "arquivo.close()\n",
        "dna"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'CAACTCTGCGAGTGCAGTCTATACGAGTCTAGACCCGATGGTACCCAAAATGGCCGAGAGTACGGATAGGAAATCTTACAATCAGAAAAGTTCGATCCTTATATGCACTTATGAGGGGTAGAAAAGTCACCATGGTTAAGAAACGGGTGTGAATCAGGATCCTTATTCTTACCTTTAAAAGGCCCAGCGGGTCAAGTATCTTGTCGAGTGATAGAAAATTTTGTCGACGACTGGATTAAAGGCTAATGTCTAGGTCTGGCCAGAGTGGCGACGCAGTAGCGCTTGCGGAACTCCGGATGACCTTGAGTGTAACCTTACATAATATGGGTCAAGGTTTCTAAGTTTTGGAGACCTAACCTTCCACGGTAGTGGTGGCTCTATAAATCACCGGGCTGGGCGAGTCGCAGAAGCTTGTGAAAACGAGTCACCTCAATACTCTAGGAGCGATCTTGAACGGGCACGACAGCAATGAGCAAGCGGTCCAATAGAAGCTCCCCCAAGTTAGCAGCGTGCTGACCTTTTGGGATGTGAGTTGATCTCCATCAAGTCTTAGTAGTTCCCTCGTGTGGGTTGCTACGCGATACAACGGGCATGGATGTTAAATCCCTCTAGAGTCGGATCCTAAGAGGAACAGTAAACCCCTAATTTCGGTGAACCAGGGGTTTGAATTATGTGATACGCCTTCGCGTTAACGCGCGAGCTAAAGCAGTCAGCGCCATCGGGATAGCGGTTATAGACCAAGGATCTGGTCAGAGGACATGGCCACAGGCGTATAGGTTAGTGTAGGACTGCGCCCGTTGTAACCTTGTATTGTAGCCTGGACTGTCTAAATCGATTTTCCCAATCGTATAACTGGGTCACGGCCTGGATGGAGTGCGAGTACATCGCATAGACTGGTTCAATACAGAATGTGGTCTATATCTCAGCTGTCCACCGTCGGTCTCATGTGCCATGAAGGTCTCG\\n'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 129
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ESSmgMq0gS5c",
        "outputId": "31cf9bb2-1c65-4418-dae1-d248f88382c3"
      },
      "source": [
        "# contar cada caracter da string\n",
        "Counter(dna)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Counter({'\\n': 1, 'A': 252, 'C': 210, 'G': 259, 'T': 242})"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iIYylQD8hqUA"
      },
      "source": [
        "###Transcribing DNA into RNA"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 154
        },
        "id": "yr6fYn8Uhr7O",
        "outputId": "14736b65-d7e2-473d-9a1b-6f54ba0b9c85"
      },
      "source": [
        "arquivo = open(\"/content/rosalind_rna.txt\", \"r\")\n",
        "dna = arquivo.read()\n",
        "arquivo.close()\n",
        "dna"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'GACACACTGTATTTTGGTAAACTTCTTGTTTCTCCAGTGTATTGGGGGGGGGTCATGGAAGGACTAAGATGTAGCCCGGACGACAACAACGTTCCTGAAGGCGCGCTAAGAATGCCCGACTGCCGACTTAAGAGTGTGCAGTAACGAAGTGGACTTTATGCCACGCAAGTCCCCCATTTCCGTTGGCAGCCGTTATCTGGCGAGAACGCGAGGAAGCAGTATAATATAAAGGCTCCTTGTATAAGTATTGTGAGAATCTATCCTGATGTGACATGTTGTGGATCCGGAATTATGCTACTGCCTCAGAGGGGCTTTCTAGTAAGTGGGCCTACGGGTGAACTATGAGCCCGGCTCACCAATACTATACGGGATGGATCAGCTAAGGATCACGTAAACCTTACTCCCAATGGCCGCTACCTTCGAACCTTGTAGTACTTTTAAACGCCAATACCCATTTATTATTGGCTCCAATATTTCGTTTGTCGGGAGTGATTACGTAGCGGGGTTCGGGAGGAGTTGACCGGGGGGCATCTTAGACGACCGTAGACGCTGCCCCCGGTTGCCGAGTATCTACTTCGTCATTCATAATTCAGCACGATGTTATATACGGTACACAGCGTCTGGAGAGTAGAGGTGGTGTGGCGCTGCGAAAAGACGATTGCAAGGAATCACAAGTCCGGAGAGAACTCTACGAAAGGTAGCGAGCCAATACAGAAGTTAGCTGTCGAATCCTGACACTCTGAACTGGTTAAACTACGGTCTTAGCGGTCGGAAAAAGCGGAACTCTGTTTCCTTTCCATTTCCCTATGGAAAACCGAGCCTCGGGCAATCGGCCTGCTGTTGTAGCCTAGACCCCTCAAGGTCTCTGCACCTCGAGAACCATTCTTCTAGCGTCTAATTACGTCAAAAATATTTCAAGTGCA\\n'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 130
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 154
        },
        "id": "KmuFpFP6h3os",
        "outputId": "8c377131-98f5-4433-b0e0-39697c1444e3"
      },
      "source": [
        "# substituir T por U\n",
        "dna.replace(\"T\", \"U\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'GACACACUGUAUUUUGGUAAACUUCUUGUUUCUCCAGUGUAUUGGGGGGGGGUCAUGGAAGGACUAAGAUGUAGCCCGGACGACAACAACGUUCCUGAAGGCGCGCUAAGAAUGCCCGACUGCCGACUUAAGAGUGUGCAGUAACGAAGUGGACUUUAUGCCACGCAAGUCCCCCAUUUCCGUUGGCAGCCGUUAUCUGGCGAGAACGCGAGGAAGCAGUAUAAUAUAAAGGCUCCUUGUAUAAGUAUUGUGAGAAUCUAUCCUGAUGUGACAUGUUGUGGAUCCGGAAUUAUGCUACUGCCUCAGAGGGGCUUUCUAGUAAGUGGGCCUACGGGUGAACUAUGAGCCCGGCUCACCAAUACUAUACGGGAUGGAUCAGCUAAGGAUCACGUAAACCUUACUCCCAAUGGCCGCUACCUUCGAACCUUGUAGUACUUUUAAACGCCAAUACCCAUUUAUUAUUGGCUCCAAUAUUUCGUUUGUCGGGAGUGAUUACGUAGCGGGGUUCGGGAGGAGUUGACCGGGGGGCAUCUUAGACGACCGUAGACGCUGCCCCCGGUUGCCGAGUAUCUACUUCGUCAUUCAUAAUUCAGCACGAUGUUAUAUACGGUACACAGCGUCUGGAGAGUAGAGGUGGUGUGGCGCUGCGAAAAGACGAUUGCAAGGAAUCACAAGUCCGGAGAGAACUCUACGAAAGGUAGCGAGCCAAUACAGAAGUUAGCUGUCGAAUCCUGACACUCUGAACUGGUUAAACUACGGUCUUAGCGGUCGGAAAAAGCGGAACUCUGUUUCCUUUCCAUUUCCCUAUGGAAAACCGAGCCUCGGGCAAUCGGCCUGCUGUUGUAGCCUAGACCCCUCAAGGUCUCUGCACCUCGAGAACCAUUCUUCUAGCGUCUAAUUACGUCAAAAAUAUUUCAAGUGCA\\n'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 128
        }
      ]
    }
  ]
}
