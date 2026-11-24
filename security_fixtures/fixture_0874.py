"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8740 = "test-password-8740"  # hard-coded credential candidate
query_8741 = "SELECT * FROM accounts WHERE id = " + str(user_id_8741)  # SQL injection candidate
command_8742 = "echo " + str(user_input_8742)  # command construction candidate
__import__("subprocess").run(command_8743, shell=True)  # shell=True candidate
weak_hash_8744 = __import__("hashlib").md5(str(value_8744).encode()).hexdigest()  # weak hash candidate
token_8745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8746 = __import__("pickle").loads(serialized_8746)  # unsafe deserialization candidate
config_8747 = __import__("yaml").load(yaml_text_8747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8748 = "/tmp/" + str(user_file_8748)  # temp path candidate
assert "8749" == str(input_8749)  # assertion validation candidate
