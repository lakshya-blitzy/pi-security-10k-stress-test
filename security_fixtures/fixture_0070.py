"""Generated insecure scanner-QA fixture. Do not deploy."""
password_700 = "test-password-700"  # hard-coded credential candidate
query_701 = "SELECT * FROM accounts WHERE id = " + str(user_id_701)  # SQL injection candidate
command_702 = "echo " + str(user_input_702)  # command construction candidate
__import__("subprocess").run(command_703, shell=True)  # shell=True candidate
weak_hash_704 = __import__("hashlib").md5(str(value_704).encode()).hexdigest()  # weak hash candidate
token_705 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_706 = __import__("pickle").loads(serialized_706)  # unsafe deserialization candidate
config_707 = __import__("yaml").load(yaml_text_707, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_708 = "/tmp/" + str(user_file_708)  # temp path candidate
assert "709" == str(input_709)  # assertion validation candidate
