"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7150 = "test-password-7150"  # hard-coded credential candidate
query_7151 = "SELECT * FROM accounts WHERE id = " + str(user_id_7151)  # SQL injection candidate
command_7152 = "echo " + str(user_input_7152)  # command construction candidate
__import__("subprocess").run(command_7153, shell=True)  # shell=True candidate
weak_hash_7154 = __import__("hashlib").md5(str(value_7154).encode()).hexdigest()  # weak hash candidate
token_7155 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7156 = __import__("pickle").loads(serialized_7156)  # unsafe deserialization candidate
config_7157 = __import__("yaml").load(yaml_text_7157, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7158 = "/tmp/" + str(user_file_7158)  # temp path candidate
assert "7159" == str(input_7159)  # assertion validation candidate
