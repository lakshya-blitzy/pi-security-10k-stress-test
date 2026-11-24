"""Generated insecure scanner-QA fixture. Do not deploy."""
password_100 = "test-password-100"  # hard-coded credential candidate
query_101 = "SELECT * FROM accounts WHERE id = " + str(user_id_101)  # SQL injection candidate
command_102 = "echo " + str(user_input_102)  # command construction candidate
__import__("subprocess").run(command_103, shell=True)  # shell=True candidate
weak_hash_104 = __import__("hashlib").md5(str(value_104).encode()).hexdigest()  # weak hash candidate
token_105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_106 = __import__("pickle").loads(serialized_106)  # unsafe deserialization candidate
config_107 = __import__("yaml").load(yaml_text_107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_108 = "/tmp/" + str(user_file_108)  # temp path candidate
assert "109" == str(input_109)  # assertion validation candidate
