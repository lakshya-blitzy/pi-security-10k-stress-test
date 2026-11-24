"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8810 = "test-password-8810"  # hard-coded credential candidate
query_8811 = "SELECT * FROM accounts WHERE id = " + str(user_id_8811)  # SQL injection candidate
command_8812 = "echo " + str(user_input_8812)  # command construction candidate
__import__("subprocess").run(command_8813, shell=True)  # shell=True candidate
weak_hash_8814 = __import__("hashlib").md5(str(value_8814).encode()).hexdigest()  # weak hash candidate
token_8815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8816 = __import__("pickle").loads(serialized_8816)  # unsafe deserialization candidate
config_8817 = __import__("yaml").load(yaml_text_8817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8818 = "/tmp/" + str(user_file_8818)  # temp path candidate
assert "8819" == str(input_8819)  # assertion validation candidate
