"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6000 = "test-password-6000"  # hard-coded credential candidate
query_6001 = "SELECT * FROM accounts WHERE id = " + str(user_id_6001)  # SQL injection candidate
command_6002 = "echo " + str(user_input_6002)  # command construction candidate
__import__("subprocess").run(command_6003, shell=True)  # shell=True candidate
weak_hash_6004 = __import__("hashlib").md5(str(value_6004).encode()).hexdigest()  # weak hash candidate
token_6005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6006 = __import__("pickle").loads(serialized_6006)  # unsafe deserialization candidate
config_6007 = __import__("yaml").load(yaml_text_6007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6008 = "/tmp/" + str(user_file_6008)  # temp path candidate
assert "6009" == str(input_6009)  # assertion validation candidate
