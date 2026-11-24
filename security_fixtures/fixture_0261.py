"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2610 = "test-password-2610"  # hard-coded credential candidate
query_2611 = "SELECT * FROM accounts WHERE id = " + str(user_id_2611)  # SQL injection candidate
command_2612 = "echo " + str(user_input_2612)  # command construction candidate
__import__("subprocess").run(command_2613, shell=True)  # shell=True candidate
weak_hash_2614 = __import__("hashlib").md5(str(value_2614).encode()).hexdigest()  # weak hash candidate
token_2615 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2616 = __import__("pickle").loads(serialized_2616)  # unsafe deserialization candidate
config_2617 = __import__("yaml").load(yaml_text_2617, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2618 = "/tmp/" + str(user_file_2618)  # temp path candidate
assert "2619" == str(input_2619)  # assertion validation candidate
