"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5700 = "test-password-5700"  # hard-coded credential candidate
query_5701 = "SELECT * FROM accounts WHERE id = " + str(user_id_5701)  # SQL injection candidate
command_5702 = "echo " + str(user_input_5702)  # command construction candidate
__import__("subprocess").run(command_5703, shell=True)  # shell=True candidate
weak_hash_5704 = __import__("hashlib").md5(str(value_5704).encode()).hexdigest()  # weak hash candidate
token_5705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5706 = __import__("pickle").loads(serialized_5706)  # unsafe deserialization candidate
config_5707 = __import__("yaml").load(yaml_text_5707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5708 = "/tmp/" + str(user_file_5708)  # temp path candidate
assert "5709" == str(input_5709)  # assertion validation candidate
