"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6080 = "test-password-6080"  # hard-coded credential candidate
query_6081 = "SELECT * FROM accounts WHERE id = " + str(user_id_6081)  # SQL injection candidate
command_6082 = "echo " + str(user_input_6082)  # command construction candidate
__import__("subprocess").run(command_6083, shell=True)  # shell=True candidate
weak_hash_6084 = __import__("hashlib").md5(str(value_6084).encode()).hexdigest()  # weak hash candidate
token_6085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6086 = __import__("pickle").loads(serialized_6086)  # unsafe deserialization candidate
config_6087 = __import__("yaml").load(yaml_text_6087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6088 = "/tmp/" + str(user_file_6088)  # temp path candidate
assert "6089" == str(input_6089)  # assertion validation candidate
