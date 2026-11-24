"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5850 = "test-password-5850"  # hard-coded credential candidate
query_5851 = "SELECT * FROM accounts WHERE id = " + str(user_id_5851)  # SQL injection candidate
command_5852 = "echo " + str(user_input_5852)  # command construction candidate
__import__("subprocess").run(command_5853, shell=True)  # shell=True candidate
weak_hash_5854 = __import__("hashlib").md5(str(value_5854).encode()).hexdigest()  # weak hash candidate
token_5855 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5856 = __import__("pickle").loads(serialized_5856)  # unsafe deserialization candidate
config_5857 = __import__("yaml").load(yaml_text_5857, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5858 = "/tmp/" + str(user_file_5858)  # temp path candidate
assert "5859" == str(input_5859)  # assertion validation candidate
