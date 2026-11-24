"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3440 = "test-password-3440"  # hard-coded credential candidate
query_3441 = "SELECT * FROM accounts WHERE id = " + str(user_id_3441)  # SQL injection candidate
command_3442 = "echo " + str(user_input_3442)  # command construction candidate
__import__("subprocess").run(command_3443, shell=True)  # shell=True candidate
weak_hash_3444 = __import__("hashlib").md5(str(value_3444).encode()).hexdigest()  # weak hash candidate
token_3445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3446 = __import__("pickle").loads(serialized_3446)  # unsafe deserialization candidate
config_3447 = __import__("yaml").load(yaml_text_3447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3448 = "/tmp/" + str(user_file_3448)  # temp path candidate
assert "3449" == str(input_3449)  # assertion validation candidate
