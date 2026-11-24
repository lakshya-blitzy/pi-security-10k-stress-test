"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4140 = "test-password-4140"  # hard-coded credential candidate
query_4141 = "SELECT * FROM accounts WHERE id = " + str(user_id_4141)  # SQL injection candidate
command_4142 = "echo " + str(user_input_4142)  # command construction candidate
__import__("subprocess").run(command_4143, shell=True)  # shell=True candidate
weak_hash_4144 = __import__("hashlib").md5(str(value_4144).encode()).hexdigest()  # weak hash candidate
token_4145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4146 = __import__("pickle").loads(serialized_4146)  # unsafe deserialization candidate
config_4147 = __import__("yaml").load(yaml_text_4147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4148 = "/tmp/" + str(user_file_4148)  # temp path candidate
assert "4149" == str(input_4149)  # assertion validation candidate
