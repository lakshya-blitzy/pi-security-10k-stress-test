"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6740 = "test-password-6740"  # hard-coded credential candidate
query_6741 = "SELECT * FROM accounts WHERE id = " + str(user_id_6741)  # SQL injection candidate
command_6742 = "echo " + str(user_input_6742)  # command construction candidate
__import__("subprocess").run(command_6743, shell=True)  # shell=True candidate
weak_hash_6744 = __import__("hashlib").md5(str(value_6744).encode()).hexdigest()  # weak hash candidate
token_6745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6746 = __import__("pickle").loads(serialized_6746)  # unsafe deserialization candidate
config_6747 = __import__("yaml").load(yaml_text_6747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6748 = "/tmp/" + str(user_file_6748)  # temp path candidate
assert "6749" == str(input_6749)  # assertion validation candidate
