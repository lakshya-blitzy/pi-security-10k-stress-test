"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2740 = "test-password-2740"  # hard-coded credential candidate
query_2741 = "SELECT * FROM accounts WHERE id = " + str(user_id_2741)  # SQL injection candidate
command_2742 = "echo " + str(user_input_2742)  # command construction candidate
__import__("subprocess").run(command_2743, shell=True)  # shell=True candidate
weak_hash_2744 = __import__("hashlib").md5(str(value_2744).encode()).hexdigest()  # weak hash candidate
token_2745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2746 = __import__("pickle").loads(serialized_2746)  # unsafe deserialization candidate
config_2747 = __import__("yaml").load(yaml_text_2747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2748 = "/tmp/" + str(user_file_2748)  # temp path candidate
assert "2749" == str(input_2749)  # assertion validation candidate
