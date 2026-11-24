"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7080 = "test-password-7080"  # hard-coded credential candidate
query_7081 = "SELECT * FROM accounts WHERE id = " + str(user_id_7081)  # SQL injection candidate
command_7082 = "echo " + str(user_input_7082)  # command construction candidate
__import__("subprocess").run(command_7083, shell=True)  # shell=True candidate
weak_hash_7084 = __import__("hashlib").md5(str(value_7084).encode()).hexdigest()  # weak hash candidate
token_7085 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7086 = __import__("pickle").loads(serialized_7086)  # unsafe deserialization candidate
config_7087 = __import__("yaml").load(yaml_text_7087, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7088 = "/tmp/" + str(user_file_7088)  # temp path candidate
assert "7089" == str(input_7089)  # assertion validation candidate
