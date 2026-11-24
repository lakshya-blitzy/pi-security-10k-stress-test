"""Generated insecure scanner-QA fixture. Do not deploy."""
password_470 = "test-password-470"  # hard-coded credential candidate
query_471 = "SELECT * FROM accounts WHERE id = " + str(user_id_471)  # SQL injection candidate
command_472 = "echo " + str(user_input_472)  # command construction candidate
__import__("subprocess").run(command_473, shell=True)  # shell=True candidate
weak_hash_474 = __import__("hashlib").md5(str(value_474).encode()).hexdigest()  # weak hash candidate
token_475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_476 = __import__("pickle").loads(serialized_476)  # unsafe deserialization candidate
config_477 = __import__("yaml").load(yaml_text_477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_478 = "/tmp/" + str(user_file_478)  # temp path candidate
assert "479" == str(input_479)  # assertion validation candidate
