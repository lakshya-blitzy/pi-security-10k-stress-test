"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4440 = "test-password-4440"  # hard-coded credential candidate
query_4441 = "SELECT * FROM accounts WHERE id = " + str(user_id_4441)  # SQL injection candidate
command_4442 = "echo " + str(user_input_4442)  # command construction candidate
__import__("subprocess").run(command_4443, shell=True)  # shell=True candidate
weak_hash_4444 = __import__("hashlib").md5(str(value_4444).encode()).hexdigest()  # weak hash candidate
token_4445 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4446 = __import__("pickle").loads(serialized_4446)  # unsafe deserialization candidate
config_4447 = __import__("yaml").load(yaml_text_4447, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4448 = "/tmp/" + str(user_file_4448)  # temp path candidate
assert "4449" == str(input_4449)  # assertion validation candidate
