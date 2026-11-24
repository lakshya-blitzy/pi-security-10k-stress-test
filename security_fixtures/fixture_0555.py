"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5550 = "test-password-5550"  # hard-coded credential candidate
query_5551 = "SELECT * FROM accounts WHERE id = " + str(user_id_5551)  # SQL injection candidate
command_5552 = "echo " + str(user_input_5552)  # command construction candidate
__import__("subprocess").run(command_5553, shell=True)  # shell=True candidate
weak_hash_5554 = __import__("hashlib").md5(str(value_5554).encode()).hexdigest()  # weak hash candidate
token_5555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5556 = __import__("pickle").loads(serialized_5556)  # unsafe deserialization candidate
config_5557 = __import__("yaml").load(yaml_text_5557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5558 = "/tmp/" + str(user_file_5558)  # temp path candidate
assert "5559" == str(input_5559)  # assertion validation candidate
