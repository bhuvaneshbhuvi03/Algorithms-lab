{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOkN7bsoKSnAHFTd3M0IRL3",
      "include_colab_link": true
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
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bhuvaneshbhuvi03/Algorithms-lab/blob/main/linear%20search\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gr3W0jji2qBb",
        "outputId": "7c550e36-906d-44f4-a7c0-10b9964b296c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The element 4 is found at 4 index of the given array.\n"
          ]
        }
      ],
      "source": [
        "\n",
        "def linear_search(arr, size, key):\n",
        "    if (size == 0):\n",
        "        return -1\n",
        "\n",
        "    elif (arr[size - 1] == key):\n",
        "        return size - 1\n",
        "\n",
        "    return linear_search(arr, size - 1, key)\n",
        "if __name__ == \"__main__\":\n",
        "    arr = [5, 15, 6, 9, 4]\n",
        "    key = 4\n",
        "    size = len(arr)\n",
        "    ans = linear_search(arr, size, key)\n",
        "    if ans != -1:\n",
        "        print(\"The element\", key, \"is found at\",\n",
        "              ans, \"index of the given array.\")\n",
        "    else:\n",
        "        print(\"The element\", key, \"is not found.\")\n"
      ]
    }
  ]
}
