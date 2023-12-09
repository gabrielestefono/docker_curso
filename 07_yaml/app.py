import yaml

# Define o caminho absoluto para o arquivo
caminho_arquivo = r"D:\Estudos\docker_mb\07_yaml\teste.yaml"

if __name__ == "__main__":
    # Abre o arquivo usando o caminho absoluto
    with open(caminho_arquivo, "r") as stream:
        dictionary = yaml.safe_load(stream)

        for key, value in dictionary.items():
            print(key + " : " + str(value))
