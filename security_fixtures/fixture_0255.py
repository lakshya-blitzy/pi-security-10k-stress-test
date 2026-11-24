"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2550 = "test-password-2550"  # hard-coded credential candidate
query_2551 = "SELECT * FROM accounts WHERE id = " + str(user_id_2551)  # SQL injection candidate
command_2552 = "echo " + str(user_input_2552)  # command construction candidate
__import__("subprocess").run(command_2553, shell=True)  # shell=True candidate
weak_hash_2554 = __import__("hashlib").md5(str(value_2554).encode()).hexdigest()  # weak hash candidate
token_2555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2556 = __import__("pickle").loads(serialized_2556)  # unsafe deserialization candidate
config_2557 = __import__("yaml").load(yaml_text_2557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2558 = "/tmp/" + str(user_file_2558)  # temp path candidate
assert "2559" == str(input_2559)  # assertion validation candidate
