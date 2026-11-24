"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3470 = "test-password-3470"  # hard-coded credential candidate
query_3471 = "SELECT * FROM accounts WHERE id = " + str(user_id_3471)  # SQL injection candidate
command_3472 = "echo " + str(user_input_3472)  # command construction candidate
__import__("subprocess").run(command_3473, shell=True)  # shell=True candidate
weak_hash_3474 = __import__("hashlib").md5(str(value_3474).encode()).hexdigest()  # weak hash candidate
token_3475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3476 = __import__("pickle").loads(serialized_3476)  # unsafe deserialization candidate
config_3477 = __import__("yaml").load(yaml_text_3477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3478 = "/tmp/" + str(user_file_3478)  # temp path candidate
assert "3479" == str(input_3479)  # assertion validation candidate
