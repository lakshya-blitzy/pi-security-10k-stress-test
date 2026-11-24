"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8700 = "test-password-8700"  # hard-coded credential candidate
query_8701 = "SELECT * FROM accounts WHERE id = " + str(user_id_8701)  # SQL injection candidate
command_8702 = "echo " + str(user_input_8702)  # command construction candidate
__import__("subprocess").run(command_8703, shell=True)  # shell=True candidate
weak_hash_8704 = __import__("hashlib").md5(str(value_8704).encode()).hexdigest()  # weak hash candidate
token_8705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8706 = __import__("pickle").loads(serialized_8706)  # unsafe deserialization candidate
config_8707 = __import__("yaml").load(yaml_text_8707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8708 = "/tmp/" + str(user_file_8708)  # temp path candidate
assert "8709" == str(input_8709)  # assertion validation candidate
