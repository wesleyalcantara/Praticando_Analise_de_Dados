{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM6tApIz4R4dvICy+PXBbfG",
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
        "<a href=\"https://colab.research.google.com/github/wesleyalcantara/Praticando_Analise_de_Dados/blob/main/Untitled0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 236
        },
        "id": "rFbAFD9C2MrK",
        "outputId": "7968eb1f-5194-4267-addf-9beb1180779f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-e31100e6-d6e0-4576-ae6a-56bc6a2cd63d\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>NU_INSCRICAO</th>\n",
              "      <th>NU_ANO</th>\n",
              "      <th>CO_MUNICIPIO_RESIDENCIA</th>\n",
              "      <th>NO_MUNICIPIO_RESIDENCIA</th>\n",
              "      <th>CO_UF_RESIDENCIA</th>\n",
              "      <th>SG_UF_RESIDENCIA</th>\n",
              "      <th>NU_IDADE</th>\n",
              "      <th>TP_SEXO</th>\n",
              "      <th>TP_ESTADO_CIVIL</th>\n",
              "      <th>TP_COR_RACA</th>\n",
              "      <th>...</th>\n",
              "      <th>Q016</th>\n",
              "      <th>Q017</th>\n",
              "      <th>Q018</th>\n",
              "      <th>Q019</th>\n",
              "      <th>Q020</th>\n",
              "      <th>Q021</th>\n",
              "      <th>Q022</th>\n",
              "      <th>Q023</th>\n",
              "      <th>Q024</th>\n",
              "      <th>Q025</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>190001004661</td>\n",
              "      <td>2019</td>\n",
              "      <td>1506138</td>\n",
              "      <td>Redenção</td>\n",
              "      <td>15</td>\n",
              "      <td>PA</td>\n",
              "      <td>17</td>\n",
              "      <td>M</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>C</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>190001004674</td>\n",
              "      <td>2019</td>\n",
              "      <td>1504208</td>\n",
              "      <td>Marabá</td>\n",
              "      <td>15</td>\n",
              "      <td>PA</td>\n",
              "      <td>23</td>\n",
              "      <td>M</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>190001004722</td>\n",
              "      <td>2019</td>\n",
              "      <td>1501402</td>\n",
              "      <td>Belém</td>\n",
              "      <td>15</td>\n",
              "      <td>PA</td>\n",
              "      <td>35</td>\n",
              "      <td>F</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>...</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>190001004735</td>\n",
              "      <td>2019</td>\n",
              "      <td>1507300</td>\n",
              "      <td>São Félix do Xingu</td>\n",
              "      <td>15</td>\n",
              "      <td>PA</td>\n",
              "      <td>23</td>\n",
              "      <td>F</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>190001004776</td>\n",
              "      <td>2019</td>\n",
              "      <td>1500800</td>\n",
              "      <td>Ananindeua</td>\n",
              "      <td>15</td>\n",
              "      <td>PA</td>\n",
              "      <td>16</td>\n",
              "      <td>F</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>...</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>D</td>\n",
              "      <td>A</td>\n",
              "      <td>A</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 136 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e31100e6-d6e0-4576-ae6a-56bc6a2cd63d')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e31100e6-d6e0-4576-ae6a-56bc6a2cd63d button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e31100e6-d6e0-4576-ae6a-56bc6a2cd63d');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "   NU_INSCRICAO  NU_ANO  CO_MUNICIPIO_RESIDENCIA NO_MUNICIPIO_RESIDENCIA  \\\n",
              "0  190001004661    2019                  1506138                Redenção   \n",
              "1  190001004674    2019                  1504208                  Marabá   \n",
              "2  190001004722    2019                  1501402                   Belém   \n",
              "3  190001004735    2019                  1507300      São Félix do Xingu   \n",
              "4  190001004776    2019                  1500800              Ananindeua   \n",
              "\n",
              "   CO_UF_RESIDENCIA SG_UF_RESIDENCIA  NU_IDADE TP_SEXO  TP_ESTADO_CIVIL  \\\n",
              "0                15               PA        17       M                1   \n",
              "1                15               PA        23       M                1   \n",
              "2                15               PA        35       F                2   \n",
              "3                15               PA        23       F                1   \n",
              "4                15               PA        16       F                1   \n",
              "\n",
              "   TP_COR_RACA  ...  Q016  Q017 Q018  Q019 Q020  Q021  Q022  Q023  Q024  Q025  \n",
              "0            3  ...     A     A    A     A    B     A     C     A     B     B  \n",
              "1            3  ...     A     A    A     B    A     A     B     A     A     B  \n",
              "2            1  ...     A     A    A     B    A     B     B     A     A     B  \n",
              "3            3  ...     A     A    A     B    A     A     B     A     A     B  \n",
              "4            3  ...     A     A    A     B    A     A     D     A     A     B  \n",
              "\n",
              "[5 rows x 136 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "import pandas as pd\n",
        "\n",
        "fonte = \"https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true\"\n",
        "\n",
        "dados = pd.read_csv(fonte)\n",
        "dados.head()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados.shape\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OL5bMa3H5IuW",
        "outputId": "f57ede6a-9ac4-4fab-fa99-92af72861e7a"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(127380, 136)"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "dados.columns.values"
      ],
      "metadata": {
        "id": "E49paDm_6Eti"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"SG_UF_RESIDENCIA\"]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xm0Q6ezK5wrK",
        "outputId": "bfdb3173-8ae7-4f3f-e9c2-b193674074e1"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0         PA\n",
              "1         PA\n",
              "2         PA\n",
              "3         PA\n",
              "4         PA\n",
              "          ..\n",
              "127375    MG\n",
              "127376    BA\n",
              "127377    BA\n",
              "127378    BA\n",
              "127379    MG\n",
              "Name: SG_UF_RESIDENCIA, Length: 127380, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados.columns.values"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zw0apIvN6bbX",
        "outputId": "442230db-b6ec-44f1-aae5-331b4cda5d47"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['NU_INSCRICAO', 'NU_ANO', 'CO_MUNICIPIO_RESIDENCIA',\n",
              "       'NO_MUNICIPIO_RESIDENCIA', 'CO_UF_RESIDENCIA', 'SG_UF_RESIDENCIA',\n",
              "       'NU_IDADE', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA',\n",
              "       'TP_NACIONALIDADE', 'CO_MUNICIPIO_NASCIMENTO',\n",
              "       'NO_MUNICIPIO_NASCIMENTO', 'CO_UF_NASCIMENTO', 'SG_UF_NASCIMENTO',\n",
              "       'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO',\n",
              "       'IN_TREINEIRO', 'CO_ESCOLA', 'CO_MUNICIPIO_ESC',\n",
              "       'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC',\n",
              "       'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC',\n",
              "       'IN_BAIXA_VISAO', 'IN_CEGUEIRA', 'IN_SURDEZ',\n",
              "       'IN_DEFICIENCIA_AUDITIVA', 'IN_SURDO_CEGUEIRA',\n",
              "       'IN_DEFICIENCIA_FISICA', 'IN_DEFICIENCIA_MENTAL',\n",
              "       'IN_DEFICIT_ATENCAO', 'IN_DISLEXIA', 'IN_DISCALCULIA',\n",
              "       'IN_AUTISMO', 'IN_VISAO_MONOCULAR', 'IN_OUTRA_DEF', 'IN_GESTANTE',\n",
              "       'IN_LACTANTE', 'IN_IDOSO', 'IN_ESTUDA_CLASSE_HOSPITALAR',\n",
              "       'IN_SEM_RECURSO', 'IN_BRAILLE', 'IN_AMPLIADA_24', 'IN_AMPLIADA_18',\n",
              "       'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS',\n",
              "       'IN_TEMPO_ADICIONAL', 'IN_LEITURA_LABIAL', 'IN_MESA_CADEIRA_RODAS',\n",
              "       'IN_MESA_CADEIRA_SEPARADA', 'IN_APOIO_PERNA', 'IN_GUIA_INTERPRETE',\n",
              "       'IN_COMPUTADOR', 'IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_CANHOTO',\n",
              "       'IN_CADEIRA_ACOLCHOADA', 'IN_PROVA_DEITADO', 'IN_MOBILIARIO_OBESO',\n",
              "       'IN_LAMINA_OVERLAY', 'IN_PROTETOR_AURICULAR', 'IN_MEDIDOR_GLICOSE',\n",
              "       'IN_MAQUINA_BRAILE', 'IN_SOROBAN', 'IN_MARCA_PASSO', 'IN_SONDA',\n",
              "       'IN_MEDICAMENTOS', 'IN_SALA_INDIVIDUAL', 'IN_SALA_ESPECIAL',\n",
              "       'IN_SALA_ACOMPANHANTE', 'IN_MOBILIARIO_ESPECIFICO',\n",
              "       'IN_MATERIAL_ESPECIFICO', 'IN_NOME_SOCIAL', 'CO_MUNICIPIO_PROVA',\n",
              "       'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'SG_UF_PROVA',\n",
              "       'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC',\n",
              "       'TP_PRESENCA_MT', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC',\n",
              "       'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC',\n",
              "       'NU_NOTA_MT', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH',\n",
              "       'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA',\n",
              "       'TX_GABARITO_CN', 'TX_GABARITO_CH', 'TX_GABARITO_LC',\n",
              "       'TX_GABARITO_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_COMP1',\n",
              "       'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5',\n",
              "       'NU_NOTA_REDACAO', 'Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006',\n",
              "       'Q007', 'Q008', 'Q009', 'Q010', 'Q011', 'Q012', 'Q013', 'Q014',\n",
              "       'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021', 'Q022',\n",
              "       'Q023', 'Q024', 'Q025'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados [[\"SG_UF_RESIDENCIA\", \"Q025\"]]\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "UABa7cpT7JeJ",
        "outputId": "fbb74d0b-9429-421e-f0c8-e2d83bf908e1"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-fffbbee5-79e1-4b07-949c-3b425c1229af\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>SG_UF_RESIDENCIA</th>\n",
              "      <th>Q025</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>PA</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>PA</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>PA</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>PA</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>PA</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>127375</th>\n",
              "      <td>MG</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>127376</th>\n",
              "      <td>BA</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>127377</th>\n",
              "      <td>BA</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>127378</th>\n",
              "      <td>BA</td>\n",
              "      <td>A</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>127379</th>\n",
              "      <td>MG</td>\n",
              "      <td>B</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>127380 rows × 2 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-fffbbee5-79e1-4b07-949c-3b425c1229af')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-fffbbee5-79e1-4b07-949c-3b425c1229af button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-fffbbee5-79e1-4b07-949c-3b425c1229af');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "       SG_UF_RESIDENCIA Q025\n",
              "0                    PA    B\n",
              "1                    PA    B\n",
              "2                    PA    B\n",
              "3                    PA    B\n",
              "4                    PA    B\n",
              "...                 ...  ...\n",
              "127375               MG    B\n",
              "127376               BA    B\n",
              "127377               BA    B\n",
              "127378               BA    A\n",
              "127379               MG    B\n",
              "\n",
              "[127380 rows x 2 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"SG_UF_RESIDENCIA\"].unique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yjmhB9mU7cPn",
        "outputId": "e412198c-b189-45ba-fe8f-d2707da9a8df"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['PA', 'RO', 'MT', 'AC', 'AM', 'RR', 'MA', 'PR', 'BA', 'PI', 'CE',\n",
              "       'PE', 'AP', 'TO', 'SC', 'GO', 'MG', 'SP', 'SE', 'RJ', 'PB', 'AL',\n",
              "       'RN', 'ES', 'DF', 'RS', 'MS'], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(dados[\"SG_UF_RESIDENCIA\"].unique())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fKBusSGF7yOv",
        "outputId": "245b72c4-486f-4217-c17e-22d39df9e8d7"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "27"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"SG_UF_RESIDENCIA\"].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SsFKcP3b8H1Q",
        "outputId": "a02fad39-cd1c-4e81-b4bf-63238f936646"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "SP    20264\n",
              "MG    13547\n",
              "BA    10040\n",
              "RJ     8467\n",
              "CE     7381\n",
              "PA     7170\n",
              "PE     6941\n",
              "MA     5543\n",
              "RS     5466\n",
              "PR     5259\n",
              "GO     4268\n",
              "PB     3690\n",
              "PI     3034\n",
              "RN     2959\n",
              "AM     2820\n",
              "SC     2673\n",
              "ES     2550\n",
              "DF     2408\n",
              "AL     2263\n",
              "MT     2230\n",
              "SE     1815\n",
              "MS     1655\n",
              "RO     1400\n",
              "TO     1178\n",
              "AP     1047\n",
              "AC      946\n",
              "RR      366\n",
              "Name: SG_UF_RESIDENCIA, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"NU_IDADE\"].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x5lbEtqs8sHU",
        "outputId": "4e1ac33a-a86b-436d-9ae4-d1773234d11e"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "18    21452\n",
              "17    21256\n",
              "19    14418\n",
              "20    10413\n",
              "16     7830\n",
              "      ...  \n",
              "73        2\n",
              "75        2\n",
              "77        1\n",
              "82        1\n",
              "76        1\n",
              "Name: NU_IDADE, Length: 65, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"NU_IDADE\"].value_counts().sort_index()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZwCfive79IsH",
        "outputId": "0ef265ad-f943-41e7-960e-4fde42c1bd4b"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "13        4\n",
              "14      141\n",
              "15     2009\n",
              "16     7830\n",
              "17    21256\n",
              "      ...  \n",
              "73        2\n",
              "75        2\n",
              "76        1\n",
              "77        1\n",
              "82        1\n",
              "Name: NU_IDADE, Length: 65, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"NU_IDADE\"].hist()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 285
        },
        "id": "XWDMJzmP-UR3",
        "outputId": "1ee896de-83c8-493f-a34e-714d96148aeb"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f3a6225c450>"
            ]
          },
          "metadata": {},
          "execution_count": 21
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"NU_IDADE\"].hist(bins=20, figsize = (10,8))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 500
        },
        "id": "pleoxM8Z-yuv",
        "outputId": "8f439c61-0e8d-4cda-b201-09080307e0f1"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f3a619673d0>"
            ]
          },
          "metadata": {},
          "execution_count": 27
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Desafio01: Proporção de inscritos por idade.\n",
        "\n",
        "Desafio02: Descobrir de quais estados são os inscritos com 13 anos.\n",
        "\n",
        "Desafio03: Colocar um título no gráfico.\n",
        "\n",
        "Desafio04: Plotar os Histogramas das idades dos treineiros e não treineiros.\n",
        "\n",
        "Desafio05: Comparar as distribuições das provas de inglês e esoanhol.\n",
        "\n",
        "Desafio06: Explorar as documentações e vizualizações."
      ],
      "metadata": {
        "id": "oH0F7MAs9k3i"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dados.query(\"IN_TREINEIRO == 1\")[\"NU_IDADE\"].value_counts().sort_index()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bn7tOTcbAcav",
        "outputId": "dc39209f-7f8d-4e28-88bc-bfa5382f8f1b"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "14      64\n",
              "15    1927\n",
              "16    7142\n",
              "17    4901\n",
              "18     858\n",
              "19     228\n",
              "20      83\n",
              "21      44\n",
              "22      30\n",
              "23      21\n",
              "24      13\n",
              "25       8\n",
              "26      13\n",
              "27       9\n",
              "28       6\n",
              "29      10\n",
              "30       4\n",
              "31       4\n",
              "32       2\n",
              "33       1\n",
              "34       3\n",
              "35       2\n",
              "36       2\n",
              "37       1\n",
              "38       4\n",
              "39       2\n",
              "40       4\n",
              "41       1\n",
              "42       4\n",
              "44       2\n",
              "45       1\n",
              "46       2\n",
              "47       1\n",
              "48       1\n",
              "51       1\n",
              "55       1\n",
              "62       1\n",
              "Name: NU_IDADE, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from pandas.core.nanops import na_accum_func\n",
        "dados[\"NU_NOTA_REDACAO\"].hist(bins = 20, figsize = (8,6))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "id": "peocDohSCZLD",
        "outputId": "6831a356-f851-472d-bfb7-3df1eecc3fb2"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f3a61a714d0>"
            ]
          },
          "metadata": {},
          "execution_count": 35
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 576x432 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[\"NU_NOTA_REDACAO\"].mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KfmUJpFSDJ6W",
        "outputId": "984debbb-8f1a-4187-cb71-f54555012cf6"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "571.5700253970197"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "provas = [\"NU_NOTA_CN\",\"NU_NOTA_CH\",\"NU_NOTA_MT\",\"NU_NOTA_LC\",\"NU_NOTA_REDACAO\"]\n",
        "\n",
        "dados[provas].describe()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "YGYwlu5xDiES",
        "outputId": "6b54278e-e8b1-4f0a-d810-ba5d41d05812"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-e0849d19-4f45-4c88-8ad3-fe0feccd7ded\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>NU_NOTA_CN</th>\n",
              "      <th>NU_NOTA_CH</th>\n",
              "      <th>NU_NOTA_MT</th>\n",
              "      <th>NU_NOTA_LC</th>\n",
              "      <th>NU_NOTA_REDACAO</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>92758.000000</td>\n",
              "      <td>98043.000000</td>\n",
              "      <td>92758.000000</td>\n",
              "      <td>98043.000000</td>\n",
              "      <td>98043.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>477.964015</td>\n",
              "      <td>507.365912</td>\n",
              "      <td>523.555206</td>\n",
              "      <td>520.463928</td>\n",
              "      <td>571.570025</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>76.296099</td>\n",
              "      <td>82.972839</td>\n",
              "      <td>109.416939</td>\n",
              "      <td>64.556578</td>\n",
              "      <td>188.076455</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>418.000000</td>\n",
              "      <td>447.900000</td>\n",
              "      <td>435.300000</td>\n",
              "      <td>483.700000</td>\n",
              "      <td>480.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>470.200000</td>\n",
              "      <td>510.900000</td>\n",
              "      <td>501.600000</td>\n",
              "      <td>526.100000</td>\n",
              "      <td>580.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>533.300000</td>\n",
              "      <td>567.100000</td>\n",
              "      <td>598.200000</td>\n",
              "      <td>565.100000</td>\n",
              "      <td>680.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>797.300000</td>\n",
              "      <td>809.400000</td>\n",
              "      <td>985.000000</td>\n",
              "      <td>801.700000</td>\n",
              "      <td>1000.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e0849d19-4f45-4c88-8ad3-fe0feccd7ded')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-e0849d19-4f45-4c88-8ad3-fe0feccd7ded button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-e0849d19-4f45-4c88-8ad3-fe0feccd7ded');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "         NU_NOTA_CN    NU_NOTA_CH    NU_NOTA_MT    NU_NOTA_LC  NU_NOTA_REDACAO\n",
              "count  92758.000000  98043.000000  92758.000000  98043.000000     98043.000000\n",
              "mean     477.964015    507.365912    523.555206    520.463928       571.570025\n",
              "std       76.296099     82.972839    109.416939     64.556578       188.076455\n",
              "min        0.000000      0.000000      0.000000      0.000000         0.000000\n",
              "25%      418.000000    447.900000    435.300000    483.700000       480.000000\n",
              "50%      470.200000    510.900000    501.600000    526.100000       580.000000\n",
              "75%      533.300000    567.100000    598.200000    565.100000       680.000000\n",
              "max      797.300000    809.400000    985.000000    801.700000      1000.000000"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dados[provas].boxplot(grid=True, figsize= (10,8))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 556
        },
        "id": "k94aBLT1GmnK",
        "outputId": "0a3932f4-1240-446f-defe-27c8b23556df"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/matplotlib/cbook/__init__.py:1376: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.\n",
            "  X = np.atleast_1d(X.T if isinstance(X, np.ndarray) else np.asarray(X))\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7f3a6179ead0>"
            ]
          },
          "metadata": {},
          "execution_count": 41
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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9m/73CsYfpOHXKxfv/7ACSs33HCDQzEYGDM5huvTVfXBJH+fZH+Sz2ZiZOruJHdW1X/rtW3uvWRzkvdW1c4kD2fijMaRs3///uzfv/+gKcXJNgbDmWeemd27d+c1r3lNzjrrrJx55pnZuXNnv7sFQ+/SSy/NpZdemrGxsZEcIWGwzehK862165Ncf0jzF5K84DDr7k3yqpnsb1js2bMnjz76aJLkS1/6UhYscP3ZQfLoo4/mzjvvPDBCecklI/l/BwCmwa195lhVZXx8PFWV1tpBywyGBx98MBdccMGBZYEZgGPxl2KOTR62dvLJJx/0fQQPZxtIp556asbHxw9qGx8fz6mnntqnHgEwCASuPnj605+eRx55JEnyyCOP5OlPf3qfe8Tx+u53vzutdgBIBK6++PrXv55169blwx/+cNatW5evf/3r/e4Sx6m1lsWLF2fFihWpqqxYsSKLFy82QgnAUTmGq09uvvnm3Hzzzf3uBidg8ni7Q78DwJEY4YJp2rdvX3bv3p3x8fHs3r07+/bt63eXAJjnBC44AZPHbDl2C4DjIXABAHRM4AIA6JjABQDQMYELgIGwZcuWnH322Vm7dm3OPvvsbNmypd9dguPmshAAzHtbtmzJm970pmzevPnAfUyvuOKKJBM3tYb5zggXAPPeDTfckM2bN2fNmjVZtGhR1qxZk82bN+eGG27od9fguAhcAMx7O3bsyK5duw6aUty1a1d27NjR767BcTGlCMC89/SnPz3XXHNN/uRP/uTAlOKv/uqvuhctA8MIFwAD4dDbaLmtFoPECBcjb7Z+aU9nO252DdPz9a9/PRdccEHWrl2b1lqqKmvXrs0nPvGJfncNjovAxcibTvg5WqgSoqA7J598crZt25a3ve1tWblyZbZv355rrrkmJ598cr+7BsfFlCJMw7Jly6bVDsyORx99NE95ylNy3nnnZdGiRTnvvPPylKc8JY8++mi/uwbHxQgXTMOePXvy5Cc/OY899tiBtmXLlmXPnj197BUMv/379+e0007LBRdccKBt5cqVbiDPwDDCBdO0Z8+etNbyrA0fSWtN2II5UFXZvn17TjnllCTJKaecku3btztwnoEhcAEw700eI3nJJZfkwx/+cC655JKD2mG+M6UIwEB48pOfnJtvvjk333zzgWUjzAwKI1wADITJYygTYYvBI3ABMDAm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ZHOSHa21m6Y8tTXJZb3HlyW5a0r7r/fOVnxRkt1Tph4BAIbWTEa4fj7JryW5v6o+12u7Lslbk7y/qq5I8uUkr+4995dJXpZkZ5LHk/zmDPYNADAwTjhwtdb+Jkkd4em1h1m/JXn9ie4PAGBQudI8AEDHBC4AgI4JXAAAHZvxdbgAgNEz9bqb037txum/ZuJQ8MFlhAsAmLbW2gl9bdu27YReN+gELgCAjglcAAAdE7gAADrmoHkAoHOHO8h+GI7NOl5GuACATk0NW5dffvlh24edwAUAzInWWn7t135tpEa2JglcAEDnNm7ceNTlYSdwAQCd27Bhw1GXh53ABQDMiarKe9/73pE6dmuSwAUAdGrqMVu33377YduHncAFAHTucLf2GSWuwwUAdG7BggUHhayqyvj4eB97NLeMcAEAnZoMW0uXLs273vWuLF26NK21LFgwOjFkdN4pANAXk2HriSeeyE//9E/niSeeOBC6RoXABQB0bmxs7KjLw07gAgA6t3r16qMuDzuBCwDoVFVl7969Oemkk/LAAw/kpJNOyt69e0fqelzOUgQAOjU+Pp4FCxZk7969ecMb3pDEWYoAALNufHz8oOtwjVLYSgQuAGAOnHvuuamqrFmzJlWVc889t99dmlMCFwDQqXPPPTf3339/XvGKV+Qv/uIv8opXvCL333//SIUugQsA6NRk2Lrrrrty8skn56677joQukaFwAUAdG7z5s1HXR52AhcA0LkrrrjiqMvDTuACADp1zjnnZOvWrbnooovyyCOP5KKLLsrWrVtzzjnn9Ltrc8Z1uACATt13330599xzs3Xr1mzdujXJRAi77777+tyzuWOECwDo3H333XfQdbhGKWwlAhcAMAfWr1+fpUuXZs2aNVm6dGnWr1/f7y7NKVOKAECn1q9fn1tuuSUbN27MypUrs3379mzYsCFJsmnTpj73bm4Y4QIAOnXbbbdl48aNufrqq7N06dJcffXV2bhxY2677bZ+d23OCFwAQKf27duXdevWHdS2bt267Nu3r089mnsCFwDQqSVLluSWW245qO2WW27JkiVL+tSjuecYLgCgU1deeeWBY7ZWrlyZm266KRs2bPiRUa9hJnABAJ2aPDD+uuuuy759+7JkyZKsW7duZA6YT0wpAgB0zggXANApl4UwwgUAdMxlIQQuAKBjLgshcAEAHXNZ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\n",
            "text/plain": [
              "<Figure size 720x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}
