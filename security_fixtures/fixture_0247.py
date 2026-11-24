"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2470 = "test-password-2470"  # hard-coded credential candidate
query_2471 = "SELECT * FROM accounts WHERE id = " + str(user_id_2471)  # SQL injection candidate
command_2472 = "echo " + str(user_input_2472)  # command construction candidate
__import__("subprocess").run(command_2473, shell=True)  # shell=True candidate
weak_hash_2474 = __import__("hashlib").md5(str(value_2474).encode()).hexdigest()  # weak hash candidate
token_2475 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2476 = __import__("pickle").loads(serialized_2476)  # unsafe deserialization candidate
config_2477 = __import__("yaml").load(yaml_text_2477, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2478 = "/tmp/" + str(user_file_2478)  # temp path candidate
assert "2479" == str(input_2479)  # assertion validation candidate
