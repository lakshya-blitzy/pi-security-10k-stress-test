"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8030 = "test-password-8030"  # hard-coded credential candidate
query_8031 = "SELECT * FROM accounts WHERE id = " + str(user_id_8031)  # SQL injection candidate
command_8032 = "echo " + str(user_input_8032)  # command construction candidate
__import__("subprocess").run(command_8033, shell=True)  # shell=True candidate
weak_hash_8034 = __import__("hashlib").md5(str(value_8034).encode()).hexdigest()  # weak hash candidate
token_8035 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8036 = __import__("pickle").loads(serialized_8036)  # unsafe deserialization candidate
config_8037 = __import__("yaml").load(yaml_text_8037, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8038 = "/tmp/" + str(user_file_8038)  # temp path candidate
assert "8039" == str(input_8039)  # assertion validation candidate
