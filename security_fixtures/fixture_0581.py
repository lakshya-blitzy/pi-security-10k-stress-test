"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5810 = "test-password-5810"  # hard-coded credential candidate
query_5811 = "SELECT * FROM accounts WHERE id = " + str(user_id_5811)  # SQL injection candidate
command_5812 = "echo " + str(user_input_5812)  # command construction candidate
__import__("subprocess").run(command_5813, shell=True)  # shell=True candidate
weak_hash_5814 = __import__("hashlib").md5(str(value_5814).encode()).hexdigest()  # weak hash candidate
token_5815 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5816 = __import__("pickle").loads(serialized_5816)  # unsafe deserialization candidate
config_5817 = __import__("yaml").load(yaml_text_5817, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5818 = "/tmp/" + str(user_file_5818)  # temp path candidate
assert "5819" == str(input_5819)  # assertion validation candidate
