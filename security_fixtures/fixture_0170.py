"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1700 = "test-password-1700"  # hard-coded credential candidate
query_1701 = "SELECT * FROM accounts WHERE id = " + str(user_id_1701)  # SQL injection candidate
command_1702 = "echo " + str(user_input_1702)  # command construction candidate
__import__("subprocess").run(command_1703, shell=True)  # shell=True candidate
weak_hash_1704 = __import__("hashlib").md5(str(value_1704).encode()).hexdigest()  # weak hash candidate
token_1705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1706 = __import__("pickle").loads(serialized_1706)  # unsafe deserialization candidate
config_1707 = __import__("yaml").load(yaml_text_1707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1708 = "/tmp/" + str(user_file_1708)  # temp path candidate
assert "1709" == str(input_1709)  # assertion validation candidate
