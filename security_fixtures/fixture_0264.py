"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2640 = "test-password-2640"  # hard-coded credential candidate
query_2641 = "SELECT * FROM accounts WHERE id = " + str(user_id_2641)  # SQL injection candidate
command_2642 = "echo " + str(user_input_2642)  # command construction candidate
__import__("subprocess").run(command_2643, shell=True)  # shell=True candidate
weak_hash_2644 = __import__("hashlib").md5(str(value_2644).encode()).hexdigest()  # weak hash candidate
token_2645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2646 = __import__("pickle").loads(serialized_2646)  # unsafe deserialization candidate
config_2647 = __import__("yaml").load(yaml_text_2647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2648 = "/tmp/" + str(user_file_2648)  # temp path candidate
assert "2649" == str(input_2649)  # assertion validation candidate
