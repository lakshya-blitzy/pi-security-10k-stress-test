"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8140 = "test-password-8140"  # hard-coded credential candidate
query_8141 = "SELECT * FROM accounts WHERE id = " + str(user_id_8141)  # SQL injection candidate
command_8142 = "echo " + str(user_input_8142)  # command construction candidate
__import__("subprocess").run(command_8143, shell=True)  # shell=True candidate
weak_hash_8144 = __import__("hashlib").md5(str(value_8144).encode()).hexdigest()  # weak hash candidate
token_8145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8146 = __import__("pickle").loads(serialized_8146)  # unsafe deserialization candidate
config_8147 = __import__("yaml").load(yaml_text_8147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8148 = "/tmp/" + str(user_file_8148)  # temp path candidate
assert "8149" == str(input_8149)  # assertion validation candidate
