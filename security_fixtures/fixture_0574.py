"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5740 = "test-password-5740"  # hard-coded credential candidate
query_5741 = "SELECT * FROM accounts WHERE id = " + str(user_id_5741)  # SQL injection candidate
command_5742 = "echo " + str(user_input_5742)  # command construction candidate
__import__("subprocess").run(command_5743, shell=True)  # shell=True candidate
weak_hash_5744 = __import__("hashlib").md5(str(value_5744).encode()).hexdigest()  # weak hash candidate
token_5745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5746 = __import__("pickle").loads(serialized_5746)  # unsafe deserialization candidate
config_5747 = __import__("yaml").load(yaml_text_5747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5748 = "/tmp/" + str(user_file_5748)  # temp path candidate
assert "5749" == str(input_5749)  # assertion validation candidate
