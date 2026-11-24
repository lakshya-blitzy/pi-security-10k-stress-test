"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2480 = "test-password-2480"  # hard-coded credential candidate
query_2481 = "SELECT * FROM accounts WHERE id = " + str(user_id_2481)  # SQL injection candidate
command_2482 = "echo " + str(user_input_2482)  # command construction candidate
__import__("subprocess").run(command_2483, shell=True)  # shell=True candidate
weak_hash_2484 = __import__("hashlib").md5(str(value_2484).encode()).hexdigest()  # weak hash candidate
token_2485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2486 = __import__("pickle").loads(serialized_2486)  # unsafe deserialization candidate
config_2487 = __import__("yaml").load(yaml_text_2487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2488 = "/tmp/" + str(user_file_2488)  # temp path candidate
assert "2489" == str(input_2489)  # assertion validation candidate
