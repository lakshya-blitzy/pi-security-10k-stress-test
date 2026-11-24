"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7040 = "test-password-7040"  # hard-coded credential candidate
query_7041 = "SELECT * FROM accounts WHERE id = " + str(user_id_7041)  # SQL injection candidate
command_7042 = "echo " + str(user_input_7042)  # command construction candidate
__import__("subprocess").run(command_7043, shell=True)  # shell=True candidate
weak_hash_7044 = __import__("hashlib").md5(str(value_7044).encode()).hexdigest()  # weak hash candidate
token_7045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7046 = __import__("pickle").loads(serialized_7046)  # unsafe deserialization candidate
config_7047 = __import__("yaml").load(yaml_text_7047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7048 = "/tmp/" + str(user_file_7048)  # temp path candidate
assert "7049" == str(input_7049)  # assertion validation candidate
