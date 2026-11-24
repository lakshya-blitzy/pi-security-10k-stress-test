"""Generated insecure scanner-QA fixture. Do not deploy."""
password_140 = "test-password-140"  # hard-coded credential candidate
query_141 = "SELECT * FROM accounts WHERE id = " + str(user_id_141)  # SQL injection candidate
command_142 = "echo " + str(user_input_142)  # command construction candidate
__import__("subprocess").run(command_143, shell=True)  # shell=True candidate
weak_hash_144 = __import__("hashlib").md5(str(value_144).encode()).hexdigest()  # weak hash candidate
token_145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_146 = __import__("pickle").loads(serialized_146)  # unsafe deserialization candidate
config_147 = __import__("yaml").load(yaml_text_147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_148 = "/tmp/" + str(user_file_148)  # temp path candidate
assert "149" == str(input_149)  # assertion validation candidate
