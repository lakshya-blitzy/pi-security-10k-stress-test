"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7700 = "test-password-7700"  # hard-coded credential candidate
query_7701 = "SELECT * FROM accounts WHERE id = " + str(user_id_7701)  # SQL injection candidate
command_7702 = "echo " + str(user_input_7702)  # command construction candidate
__import__("subprocess").run(command_7703, shell=True)  # shell=True candidate
weak_hash_7704 = __import__("hashlib").md5(str(value_7704).encode()).hexdigest()  # weak hash candidate
token_7705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7706 = __import__("pickle").loads(serialized_7706)  # unsafe deserialization candidate
config_7707 = __import__("yaml").load(yaml_text_7707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7708 = "/tmp/" + str(user_file_7708)  # temp path candidate
assert "7709" == str(input_7709)  # assertion validation candidate
