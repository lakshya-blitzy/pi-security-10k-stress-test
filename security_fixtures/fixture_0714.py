"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7140 = "test-password-7140"  # hard-coded credential candidate
query_7141 = "SELECT * FROM accounts WHERE id = " + str(user_id_7141)  # SQL injection candidate
command_7142 = "echo " + str(user_input_7142)  # command construction candidate
__import__("subprocess").run(command_7143, shell=True)  # shell=True candidate
weak_hash_7144 = __import__("hashlib").md5(str(value_7144).encode()).hexdigest()  # weak hash candidate
token_7145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7146 = __import__("pickle").loads(serialized_7146)  # unsafe deserialization candidate
config_7147 = __import__("yaml").load(yaml_text_7147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7148 = "/tmp/" + str(user_file_7148)  # temp path candidate
assert "7149" == str(input_7149)  # assertion validation candidate
