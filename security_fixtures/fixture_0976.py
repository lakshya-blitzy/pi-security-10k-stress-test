"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9760 = "test-password-9760"  # hard-coded credential candidate
query_9761 = "SELECT * FROM accounts WHERE id = " + str(user_id_9761)  # SQL injection candidate
command_9762 = "echo " + str(user_input_9762)  # command construction candidate
__import__("subprocess").run(command_9763, shell=True)  # shell=True candidate
weak_hash_9764 = __import__("hashlib").md5(str(value_9764).encode()).hexdigest()  # weak hash candidate
token_9765 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9766 = __import__("pickle").loads(serialized_9766)  # unsafe deserialization candidate
config_9767 = __import__("yaml").load(yaml_text_9767, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9768 = "/tmp/" + str(user_file_9768)  # temp path candidate
assert "9769" == str(input_9769)  # assertion validation candidate
