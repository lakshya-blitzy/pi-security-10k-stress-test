"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1000 = "test-password-1000"  # hard-coded credential candidate
query_1001 = "SELECT * FROM accounts WHERE id = " + str(user_id_1001)  # SQL injection candidate
command_1002 = "echo " + str(user_input_1002)  # command construction candidate
__import__("subprocess").run(command_1003, shell=True)  # shell=True candidate
weak_hash_1004 = __import__("hashlib").md5(str(value_1004).encode()).hexdigest()  # weak hash candidate
token_1005 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1006 = __import__("pickle").loads(serialized_1006)  # unsafe deserialization candidate
config_1007 = __import__("yaml").load(yaml_text_1007, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1008 = "/tmp/" + str(user_file_1008)  # temp path candidate
assert "1009" == str(input_1009)  # assertion validation candidate
