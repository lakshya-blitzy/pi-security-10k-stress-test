"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7440 = "test-password-7440"  # hard-coded credential candidate
query_7441 = "SELECT * FROM accounts WHERE id = " + str(user_id_7441)  # SQL injection candidate
command_7442 = "echo " + str(user_input_7442)  # command construction candidate
__import__("subprocess").run(command_7443, shell=True)  # shell=True candidate
weak_hash_7444 = __import__("hashlib").md5(str(value_7444).encode()).hexdigest()  # weak hash candidate
token_7445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7446 = __import__("pickle").loads(serialized_7446)  # unsafe deserialization candidate
config_7447 = __import__("yaml").load(yaml_text_7447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7448 = "/tmp/" + str(user_file_7448)  # temp path candidate
assert "7449" == str(input_7449)  # assertion validation candidate
