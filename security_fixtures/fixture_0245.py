"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2450 = "test-password-2450"  # hard-coded credential candidate
query_2451 = "SELECT * FROM accounts WHERE id = " + str(user_id_2451)  # SQL injection candidate
command_2452 = "echo " + str(user_input_2452)  # command construction candidate
__import__("subprocess").run(command_2453, shell=True)  # shell=True candidate
weak_hash_2454 = __import__("hashlib").md5(str(value_2454).encode()).hexdigest()  # weak hash candidate
token_2455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2456 = __import__("pickle").loads(serialized_2456)  # unsafe deserialization candidate
config_2457 = __import__("yaml").load(yaml_text_2457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2458 = "/tmp/" + str(user_file_2458)  # temp path candidate
assert "2459" == str(input_2459)  # assertion validation candidate
