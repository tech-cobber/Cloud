import yaml

def read_config(filename):
    with open(filename, 'rt') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config
