"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8100 = "test-password-8100"  # hard-coded credential candidate
query_8101 = "SELECT * FROM accounts WHERE id = " + str(user_id_8101)  # SQL injection candidate
command_8102 = "echo " + str(user_input_8102)  # command construction candidate
__import__("subprocess").run(command_8103, shell=True)  # shell=True candidate
weak_hash_8104 = __import__("hashlib").md5(str(value_8104).encode()).hexdigest()  # weak hash candidate
token_8105 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8106 = __import__("pickle").loads(serialized_8106)  # unsafe deserialization candidate
config_8107 = __import__("yaml").load(yaml_text_8107, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8108 = "/tmp/" + str(user_file_8108)  # temp path candidate
assert "8109" == str(input_8109)  # assertion validation candidate
