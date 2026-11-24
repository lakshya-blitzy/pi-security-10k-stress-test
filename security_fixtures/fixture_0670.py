"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6700 = "test-password-6700"  # hard-coded credential candidate
query_6701 = "SELECT * FROM accounts WHERE id = " + str(user_id_6701)  # SQL injection candidate
command_6702 = "echo " + str(user_input_6702)  # command construction candidate
__import__("subprocess").run(command_6703, shell=True)  # shell=True candidate
weak_hash_6704 = __import__("hashlib").md5(str(value_6704).encode()).hexdigest()  # weak hash candidate
token_6705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6706 = __import__("pickle").loads(serialized_6706)  # unsafe deserialization candidate
config_6707 = __import__("yaml").load(yaml_text_6707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6708 = "/tmp/" + str(user_file_6708)  # temp path candidate
assert "6709" == str(input_6709)  # assertion validation candidate
