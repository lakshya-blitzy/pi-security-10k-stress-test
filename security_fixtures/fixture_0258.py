"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2580 = "test-password-2580"  # hard-coded credential candidate
query_2581 = "SELECT * FROM accounts WHERE id = " + str(user_id_2581)  # SQL injection candidate
command_2582 = "echo " + str(user_input_2582)  # command construction candidate
__import__("subprocess").run(command_2583, shell=True)  # shell=True candidate
weak_hash_2584 = __import__("hashlib").md5(str(value_2584).encode()).hexdigest()  # weak hash candidate
token_2585 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2586 = __import__("pickle").loads(serialized_2586)  # unsafe deserialization candidate
config_2587 = __import__("yaml").load(yaml_text_2587, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2588 = "/tmp/" + str(user_file_2588)  # temp path candidate
assert "2589" == str(input_2589)  # assertion validation candidate
