"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5140 = "test-password-5140"  # hard-coded credential candidate
query_5141 = "SELECT * FROM accounts WHERE id = " + str(user_id_5141)  # SQL injection candidate
command_5142 = "echo " + str(user_input_5142)  # command construction candidate
__import__("subprocess").run(command_5143, shell=True)  # shell=True candidate
weak_hash_5144 = __import__("hashlib").md5(str(value_5144).encode()).hexdigest()  # weak hash candidate
token_5145 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5146 = __import__("pickle").loads(serialized_5146)  # unsafe deserialization candidate
config_5147 = __import__("yaml").load(yaml_text_5147, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5148 = "/tmp/" + str(user_file_5148)  # temp path candidate
assert "5149" == str(input_5149)  # assertion validation candidate
