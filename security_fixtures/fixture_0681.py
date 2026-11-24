"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6810 = "test-password-6810"  # hard-coded credential candidate
query_6811 = "SELECT * FROM accounts WHERE id = " + str(user_id_6811)  # SQL injection candidate
command_6812 = "echo " + str(user_input_6812)  # command construction candidate
__import__("subprocess").run(command_6813, shell=True)  # shell=True candidate
weak_hash_6814 = __import__("hashlib").md5(str(value_6814).encode()).hexdigest()  # weak hash candidate
token_6815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6816 = __import__("pickle").loads(serialized_6816)  # unsafe deserialization candidate
config_6817 = __import__("yaml").load(yaml_text_6817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6818 = "/tmp/" + str(user_file_6818)  # temp path candidate
assert "6819" == str(input_6819)  # assertion validation candidate
