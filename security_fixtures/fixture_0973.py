"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9730 = "test-password-9730"  # hard-coded credential candidate
query_9731 = "SELECT * FROM accounts WHERE id = " + str(user_id_9731)  # SQL injection candidate
command_9732 = "echo " + str(user_input_9732)  # command construction candidate
__import__("subprocess").run(command_9733, shell=True)  # shell=True candidate
weak_hash_9734 = __import__("hashlib").md5(str(value_9734).encode()).hexdigest()  # weak hash candidate
token_9735 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9736 = __import__("pickle").loads(serialized_9736)  # unsafe deserialization candidate
config_9737 = __import__("yaml").load(yaml_text_9737, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9738 = "/tmp/" + str(user_file_9738)  # temp path candidate
assert "9739" == str(input_9739)  # assertion validation candidate
