"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7500 = "test-password-7500"  # hard-coded credential candidate
query_7501 = "SELECT * FROM accounts WHERE id = " + str(user_id_7501)  # SQL injection candidate
command_7502 = "echo " + str(user_input_7502)  # command construction candidate
__import__("subprocess").run(command_7503, shell=True)  # shell=True candidate
weak_hash_7504 = __import__("hashlib").md5(str(value_7504).encode()).hexdigest()  # weak hash candidate
token_7505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7506 = __import__("pickle").loads(serialized_7506)  # unsafe deserialization candidate
config_7507 = __import__("yaml").load(yaml_text_7507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7508 = "/tmp/" + str(user_file_7508)  # temp path candidate
assert "7509" == str(input_7509)  # assertion validation candidate
