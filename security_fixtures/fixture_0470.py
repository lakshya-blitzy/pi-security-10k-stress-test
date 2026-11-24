"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4700 = "test-password-4700"  # hard-coded credential candidate
query_4701 = "SELECT * FROM accounts WHERE id = " + str(user_id_4701)  # SQL injection candidate
command_4702 = "echo " + str(user_input_4702)  # command construction candidate
__import__("subprocess").run(command_4703, shell=True)  # shell=True candidate
weak_hash_4704 = __import__("hashlib").md5(str(value_4704).encode()).hexdigest()  # weak hash candidate
token_4705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4706 = __import__("pickle").loads(serialized_4706)  # unsafe deserialization candidate
config_4707 = __import__("yaml").load(yaml_text_4707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4708 = "/tmp/" + str(user_file_4708)  # temp path candidate
assert "4709" == str(input_4709)  # assertion validation candidate
