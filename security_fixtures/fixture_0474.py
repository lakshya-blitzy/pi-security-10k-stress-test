"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4740 = "test-password-4740"  # hard-coded credential candidate
query_4741 = "SELECT * FROM accounts WHERE id = " + str(user_id_4741)  # SQL injection candidate
command_4742 = "echo " + str(user_input_4742)  # command construction candidate
__import__("subprocess").run(command_4743, shell=True)  # shell=True candidate
weak_hash_4744 = __import__("hashlib").md5(str(value_4744).encode()).hexdigest()  # weak hash candidate
token_4745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4746 = __import__("pickle").loads(serialized_4746)  # unsafe deserialization candidate
config_4747 = __import__("yaml").load(yaml_text_4747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4748 = "/tmp/" + str(user_file_4748)  # temp path candidate
assert "4749" == str(input_4749)  # assertion validation candidate
