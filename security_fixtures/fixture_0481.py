"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4810 = "test-password-4810"  # hard-coded credential candidate
query_4811 = "SELECT * FROM accounts WHERE id = " + str(user_id_4811)  # SQL injection candidate
command_4812 = "echo " + str(user_input_4812)  # command construction candidate
__import__("subprocess").run(command_4813, shell=True)  # shell=True candidate
weak_hash_4814 = __import__("hashlib").md5(str(value_4814).encode()).hexdigest()  # weak hash candidate
token_4815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4816 = __import__("pickle").loads(serialized_4816)  # unsafe deserialization candidate
config_4817 = __import__("yaml").load(yaml_text_4817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4818 = "/tmp/" + str(user_file_4818)  # temp path candidate
assert "4819" == str(input_4819)  # assertion validation candidate
