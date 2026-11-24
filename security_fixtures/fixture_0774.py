"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7740 = "test-password-7740"  # hard-coded credential candidate
query_7741 = "SELECT * FROM accounts WHERE id = " + str(user_id_7741)  # SQL injection candidate
command_7742 = "echo " + str(user_input_7742)  # command construction candidate
__import__("subprocess").run(command_7743, shell=True)  # shell=True candidate
weak_hash_7744 = __import__("hashlib").md5(str(value_7744).encode()).hexdigest()  # weak hash candidate
token_7745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7746 = __import__("pickle").loads(serialized_7746)  # unsafe deserialization candidate
config_7747 = __import__("yaml").load(yaml_text_7747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7748 = "/tmp/" + str(user_file_7748)  # temp path candidate
assert "7749" == str(input_7749)  # assertion validation candidate
